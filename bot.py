#!/usr/bin/env python3
import os, sys
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

print("="*60)
print("🤖 POLYMARKET AUTO TRADER")
print("="*60)

# Required secrets
required = {
    'PRIVATE_KEY': 'POLYMARKET_PRIVATE_KEY',
    'WALLET_ADDRESS': 'POLYMARKET_WALLET_ADDRESS', 
    'TOKEN_ID': 'TARGET_TOKEN_ID'
}

print("Checking configuration...")
all_ok = True

for secret, env_var in required.items():
    value = os.getenv(env_var)
    if value:
        # Hide sensitive info
        if 'KEY' in env_var or 'PRIVATE' in env_var:
            display = '***' + value[-8:]
        elif 'ADDRESS' in env_var:
            display = value[:10] + '...' + value[-8:]
        else:
            display = value[:20] + '...' if len(value) > 20 else value
        
        print(f"✅ {secret}: {display}")
    else:
        print(f"❌ {secret}: NOT SET")
        all_ok = False

if not all_ok:
    print("\n❌ Missing configuration!")
    print("Please set GitHub Secrets:")
    for secret in required.keys():
        print(f"  - {secret}")
    sys.exit(1)

print("\n✅ All configuration OK")

# Trading mode
mode = os.getenv('TRADING_MODE', 'paper_live')
print(f"\n📊 Trading Mode: {mode}")
print(f"   Time: {datetime.now().strftime('%H:%M:%S')}")

if mode == 'live':
    print("\n⚠️  LIVE TRADING MODE - REAL MONEY!")
else:
    print("\nℹ️  Paper trading mode - no real money")

# Test SDK
try:
    print("\n🔧 Testing Polymarket SDK...")
    from py_clob_client.client import Client
    
    pk = os.getenv('POLYMARKET_PRIVATE_KEY')
    client = Client(
        private_key=pk,
        chain_id=137,
        host="https://clob.polymarket.com"
    )
    
    print("✅ SDK initialized successfully")
    print(f"   Chain ID: {client.chain_id}")
    print(f"   API Host: {client.host}")
    
    # Ready for trading logic
    print("\n🎯 System ready for trading!")
    print("   Add trading logic here:")
    print("   1. Market analysis")
    print("   2. Risk assessment") 
    print("   3. Order creation")
    print("   4. Trade execution")
    
except ImportError as e:
    print(f"❌ SDK import failed: {e}")
    print("   Run: pip install py-clob-client")
    sys.exit(1)
except Exception as e:
    print(f"❌ SDK error: {e}")
    sys.exit(1)

print("\n" + "="*60)
print("✅ Trading bot completed successfully!")
sys.exit(0)