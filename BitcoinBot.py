import ssl
import websocket
import json

def on_open(ws):
    print('Abriu uma conexão')
    json_subscribe ="""
{
        "event": "bts:subscribe",
        "data":{
            "channel": "live_trades_btcusd"
        }
}
"""
    ws.send(json_subscribe)

def comprar():
    pass

def vender():
    print("Você vendeu")

def on_close(ws):
    print('FECHOU CONEXAO')

def erro(ws, erro):
    print("Deu erro")
    print('Seu erro foi:', erro)


def ao_receber_mensagem(ws, mensagem):
    mensagem1 = json.loads(mensagem)
    price = mensagem1['data']['price']
    print(price)
    try:
        if price > 8000:
            vender()
        elif price < 8000:
            comprar()
        else:
            print("Aguardando")
    except Exception as e:
        print(e)

if __name__ == '__main__':
    ws = websocket.WebSocketApp("wss://ws.bitstamp.net.",
                                on_open=on_open,
                                on_close=on_close,
                                on_message=ao_receber_mensagem,
                                on_error=erro)
    ws.run_forever(sslopt={'cert_reqs': ssl.CERT_NONE})