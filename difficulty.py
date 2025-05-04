from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import json

# Save the original json.loads before patching
original_json_loads = json.loads

# Patch json.loads to ignore parse_float and avoid using Decimal
import bitcoinrpc.authproxy
def patched_json_loads(s, *args, **kwargs):
    kwargs.pop("parse_float", None)
    return original_json_loads(s, *args, **kwargs)

bitcoinrpc.authproxy.json = json
bitcoinrpc.authproxy.json.loads = patched_json_loads

# RPC credentials
rpc_user = "gilles"
rpc_password = "gilles"

# Create the RPC connection
rpc_connection = AuthServiceProxy(f"http://{rpc_user}:{rpc_password}@127.0.0.1:8332")

try:
    mining_info = rpc_connection.getmininginfo()
    print(f"Raw mining_info: {mining_info}")
    print(f"Difficulty: {mining_info.get('difficulty')}")
except JSONRPCException as json_exc:
    print(f"JSON RPC error: {json_exc}")
except Exception as e:
    print(f"Error: {e}")
