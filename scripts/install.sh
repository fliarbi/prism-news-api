#!/usr/bin/env bash
# Install the Prism News command-line client for the current user.
# Never uses sudo and never starts a service. Sets PRISM_API_BASE / PRISM_BUSINESS_API_BASE
# through ~/.config/prism/env.sh, loaded by one line in your shell startup files
# (skip with PRISM_NO_PROFILE=1).
set -euo pipefail
umask 077

# Everything runs inside main so a partly downloaded script cannot execute half the steps.
main() {
if [[ ${1:-} == --help ]]; then
  cat <<'HELP'
Install `prism-news` and `prism-business-news` (one client for both Prism News APIs).
Requires Bash, curl and Python 3.8+.
Environment:
  GH_TOKEN          GitHub token with Contents: read (only for a private fork)
  PRISM_BIN_DIR     Where the commands go (default: ~/.local/bin)
  PRISM_REF         Branch, tag or commit to install from (default: main)
  PRISM_REPO        Source repository (default: fliarbi/prism-news-api)
  PRISM_NO_PROFILE  1 = do not add the env.sh line to ~/.bashrc, ~/.zshrc, ~/.profile
Existing commands of the same name are replaced; your saved key in ~/.config/prism is kept.
HELP
  exit 0
fi
[[ $# == 0 ]] || { echo 'Use --help for installer options.' >&2; exit 2; }

repo=${PRISM_REPO:-fliarbi/prism-news-api}
ref=${PRISM_REF:-main}
bin_dir=${PRISM_BIN_DIR:-${HOME:?HOME must be set}/.local/bin}
[[ $repo =~ ^[A-Za-z0-9._-]+/[A-Za-z0-9._-]+$ ]] || { echo 'Invalid PRISM_REPO.' >&2; exit 2; }
[[ $ref =~ ^[A-Za-z0-9._/-]+$ && $ref != -* ]] || { echo 'Invalid PRISM_REF.' >&2; exit 2; }
command -v curl >/dev/null || { echo 'Install curl first.' >&2; exit 1; }
python_bin=$(command -v python3 || true)
[[ -n $python_bin ]] || { echo 'Install Python 3.8 or newer first.' >&2; exit 1; }
"$python_bin" -c 'import sys; sys.exit(0 if sys.version_info >= (3, 8) else "Python 3.8+ is required")'

stage=$(mktemp -d "${TMPDIR:-/tmp}/prism-install.XXXXXXXX")
trap 'rm -rf -- "$stage"' EXIT
token=${GH_TOKEN:-${GITHUB_TOKEN:-}}
if [[ -z $token ]] && command -v gh >/dev/null; then token=$(gh auth token 2>/dev/null || true); fi
[[ -z $token || $token =~ ^[A-Za-z0-9_]+$ ]] || { echo 'Invalid GitHub token format.' >&2; exit 2; }

# Public repositories: the raw file (no API rate limit). A token switches to the contents API,
# which also serves private forks.
url="https://raw.githubusercontent.com/$repo/$ref/scripts/prism_cli.py"
[[ -z $token ]] || url="https://api.github.com/repos/$repo/contents/scripts/prism_cli.py?ref=$ref"
echo "Downloading the Prism client from $repo ($ref)…"
# The header arrives on stdin, so the token never appears in process arguments or files.
if ! {
  printf 'header = "Accept: application/vnd.github.raw"\n'
  if [[ -n $token ]]; then printf 'header = "Authorization: Bearer %s"\n' "$token"; fi
} | curl --config - --proto '=https' --proto-redir '=https' --fail --silent --show-error --location \
    --connect-timeout 15 --max-time 120 --retry 2 \
    "$url" -o "$stage/prism_cli.py"; then
  echo "Download failed. Check your connection to github.com (a private fork also needs GH_TOKEN)." >&2
  exit 1
fi
unset token GH_TOKEN GITHUB_TOKEN
grep -q '^VERSION = ' "$stage/prism_cli.py" || { echo 'Unexpected download; nothing was installed.' >&2; exit 1; }
"$python_bin" -m py_compile "$stage/prism_cli.py"

mkdir -p -- "$bin_dir"
share=${XDG_DATA_HOME:-$HOME/.local/share}/prism-cli
mkdir -p -- "$share"
install -m 700 "$stage/prism_cli.py" "$share/prism_cli.py"
for name in prism-news prism-business-news; do
  # The launcher name picks the API.
  printf '#!/bin/sh\nPRISM_CLI_PRODUCT=%s exec "%s" "%s" "$@"\n' "$name" "$python_bin" "$share/prism_cli.py" > "$stage/$name"
  install -m 700 "$stage/$name" "$bin_dir/$name"
done
echo "Installed prism-news and prism-business-news in $bin_dir."

# Default base URLs (and the command folder on PATH) for curl, Python and the CLI.
conf_dir=${XDG_CONFIG_HOME:-$HOME/.config}/prism
mkdir -p -- "$conf_dir"
cat > "$conf_dir/env.sh" <<ENV
# Prism News APIs: written by the Prism installer. Safe to edit.
export PRISM_API_BASE="\${PRISM_API_BASE:-https://radar-api.fliarbi.com/news}"
export PRISM_BUSINESS_API_BASE="\${PRISM_BUSINESS_API_BASE:-https://radar-api.fliarbi.com/business-news}"
case ":\$PATH:" in *":$bin_dir:"*) ;; *) export PATH="$bin_dir:\$PATH" ;; esac
ENV
chmod 644 "$conf_dir/env.sh"
line="[ -f \"$conf_dir/env.sh\" ] && . \"$conf_dir/env.sh\"  # prism-news"
if [[ ${PRISM_NO_PROFILE:-0} != 1 ]]; then
  for rc in "$HOME/.bashrc" "$HOME/.zshrc" "$HOME/.profile"; do
    [[ $rc == "$HOME/.profile" || -f $rc ]] || continue
    grep -qs '# prism-news$' "$rc" || printf '\n%s\n' "$line" >> "$rc"
  done
  echo "PRISM_API_BASE and PRISM_BUSINESS_API_BASE are set for new shells (from $conf_dir/env.sh)."
else
  echo "Load the base URLs with: . $conf_dir/env.sh"
fi
cat <<NEXT

Next (open a new terminal, or run: . ${XDG_CONFIG_HOME:-$HOME/.config}/prism/env.sh):
  prism-news login        # paste your API key once; the base URLs are already set
  prism-news status
  prism-news headlines "electric vehicle" --since 2026-01-01 --until 2026-04-30 --limit 10 --table
NEXT
}

main "$@"
