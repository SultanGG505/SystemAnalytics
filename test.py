import requests
import json

# RPC настройки
rpc_user = "bitcoinuser"
rpc_password = "bitcoinsomepass456"
rpc_port = 8332  # Порт для тестовой сети
rpc_wallet = "Wallet_LR3"
rpc_url = f"http://127.0.0.1:{rpc_port}/wallet/{rpc_wallet}"

# Адрес, для которого нужно рассчитать сумму неподтвержденных транзакций
address = "tb1qwy30sdanpa9eyeld8t680avqhq9pmumnglxacu"


# Функция для вызова методов JSON RPC
def rpc_call(method, params=None):
    payload = {
        "jsonrpc": "1.0",
        "id": "python",
        "method": method,
        "params": params or []
    }
    headers = {"content-type": "text/plain;"}
    response = requests.post(rpc_url, data=json.dumps(payload), headers=headers, auth=(rpc_user, rpc_password))
    return response.json()


# Получаем список неподтвержденных транзакций
def get_unspent_sum(address):
    try:
        # listunspent метод
        unspent = rpc_call("listunspent", [1, 9999999, [address]])
        if 'error' in unspent and unspent['error']:
            print("Ошибка RPC:", unspent['error'])
            return

        transactions = unspent["result"]
        total_sum = sum(tx["amount"] for tx in transactions)
        print(f"unspent transactions: {total_sum} BTC")
    except Exception as e:
        print("Произошла ошибка:", e)


# Вызываем функцию
get_unspent_sum(address)
