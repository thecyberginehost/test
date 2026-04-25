#!/bin/bash
# Smart Contract Audit Toolkit - Setup Script
# Installs all auditing tools

set -e

echo "=== Smart Contract Audit Toolkit Setup ==="

# Check for required base tools
command -v python3 >/dev/null 2>&1 || { echo "Python3 required. Install it first."; exit 1; }
command -v pip3 >/dev/null 2>&1 || { echo "pip3 required. Install it first."; exit 1; }
command -v npm >/dev/null 2>&1 || { echo "npm required for some tools. Install Node.js first."; exit 1; }

echo ""
echo "[1/6] Installing Slither..."
pip3 install slither-analyzer 2>/dev/null || echo "  Slither install failed - try: pip3 install slither-analyzer"

echo ""
echo "[2/6] Installing Mythril..."
pip3 install mythril 2>/dev/null || echo "  Mythril install failed - try: pip3 install mythril"

echo ""
echo "[3/6] Installing Foundry (forge, cast, anvil)..."
if ! command -v forge &> /dev/null; then
    curl -L https://foundry.paradigm.xyz | bash
    export PATH="$HOME/.foundry/bin:$PATH"
    foundryup
else
    echo "  Foundry already installed: $(forge --version)"
fi

echo ""
echo "[4/6] Installing Aderyn..."
if command -v cargo &> /dev/null; then
    cargo install aderyn 2>/dev/null || echo "  Aderyn install failed via cargo"
else
    echo "  Rust/cargo not found. Install from https://rustup.rs"
    echo "  Then run: cargo install aderyn"
fi

echo ""
echo "[5/6] Installing Semgrep..."
pip3 install semgrep 2>/dev/null || echo "  Semgrep install failed - try: pip3 install semgrep"

echo ""
echo "[6/6] Installing solc-select (Solidity version manager)..."
pip3 install solc-select 2>/dev/null || echo "  solc-select install failed"
echo "  Install common versions:"
echo "    solc-select install 0.8.20 && solc-select use 0.8.20"

echo ""
echo "=== Setup Complete ==="
echo ""
echo "Verify installations:"
echo "  slither --version"
echo "  myth version"
echo "  forge --version"
echo "  aderyn --version"
echo "  semgrep --version"
echo ""
echo "Optional tools to install manually:"
echo "  - Echidna (fuzzer): https://github.com/crytic/echidna"
echo "  - Medusa (fuzzer): https://github.com/crytic/medusa"
echo "  - Halmos (symbolic): https://github.com/a16z/halmos"
echo "  - Pyrometer (abstract interp): https://github.com/nascentxyz/pyrometer"
