#!/usr/bin/env python3
import os, sys
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

print("="*50)
print("🤖 Polymarket Bot")
print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("="*50)

# Check config
keys = ['POLYMARKET_PRIVATE_KEY', 'POLYMARKET_WALLET_ADDRESS', 'TARGET_TOKEN_ID']
all_ok = True
for k in keys:
    if os.getenv(k): print(f"✅ {k}: OK")
    else: print(f"❌ {k}: Missing"); all_ok = False

if not all_ok:
    print("❌ Config incomplete")
    sys.exit(1)

print("✅ All config OK")

# Test SDK
try:
    from py_clob_client.client import Client
    client = Client(
        private_key=os.getenv('POLYMARKET_PRIVATE_KEY'),
        chain_id=137,
        host="https://clob.polymarket.com"
    )
    print("✅ SDK ready")
    print(f"Mode: {os.getenv('TRADING_MODE', 'paper_live')}")
except Exception as e:
    print(f"❌ SDK error: {e}")
    sys.exit(1)

print("🎉 Bot ready for trading!")
sys.exit(0)