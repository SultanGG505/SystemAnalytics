import requests
import json

# RPC настройки
rpc_user = "bitcoinuser"
rpc_password = "bitcoinsomepass456"
rpc_port = 8332  # Порт для тестовой сети
rpc_wallet = "Wallet_LR3"  # Имя вашего кошелька
rpc_url = f"http://127.0.0.1:{rpc_port}/wallet/{rpc_wallet}"

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

# Шаги для создания и отправки транзакции
def create_and_send_transaction(from_address, to_address, amount):
    try:
        # 1. Получить список UTXO
        utxos = rpc_call("listunspent", [1, 9999999, [from_address]])
        if utxos.get("error"):
            print("Ошибка получения UTXO:", utxos["error"])
            return
        utxos = utxos["result"]

        if not utxos:
            print("Нет доступных UTXO для создания транзакции.")
            return

        # 2. Подготовить входы для транзакции
        inputs = [{"txid": utxo["txid"], "vout": utxo["vout"]} for utxo in utxos]

        # 3. Подготовить выходы для транзакции
        outputs = {to_address: amount}
        change = sum(utxo["amount"] for utxo in utxos) - amount
        if change > 0:
            outputs[from_address] = change  # Остаток возвращается отправителю

        # 4. Создать "сырую" транзакцию
        raw_tx = rpc_call("createrawtransaction", [inputs, outputs])
        if raw_tx.get("error"):
            print("Ошибка создания raw-транзакции:", raw_tx["error"])
            return
        raw_tx_hex = raw_tx["result"]

        # 5. Подписать транзакцию
        signed_tx = rpc_call("signrawtransactionwithwallet", [raw_tx_hex])
        if signed_tx.get("error"):
            print("Ошибка подписи транзакции:", signed_tx["error"])
            return
        signed_tx_hex = signed_tx["result"]["hex"]

        # 6. Отправить транзакцию
        tx_id = rpc_call("sendrawtransaction", [signed_tx_hex])
        if tx_id.get("error"):
            print("Ошибка отправки транзакции:", tx_id["error"])
            return
        print(f"Транзакция успешно отправлена! TXID: {tx_id['result']}")

    except Exception as e:
        print("Произошла ошибка:", e)

# Адреса и сумма для транзакции
from_address = "tb1qwy30sdanpa9eyeld8t680avqhq9pmumnglxacu"
to_address = "tb1qerzrlxcfu24davlur5sqmgzzgsal6wusda40er"
amount = 0.00000890  # Сумма в BTC

# Создание и отправка транзакции
create_and_send_transaction(from_address, to_address, amount)
