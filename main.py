from websocket_async import WebSocketClient

if __name__ == '__main__':
    host = 'localhost'
    port = '80'
    websocket_resource_url = f"ws://{host}:{port}"
    ws_client = WebSocketClient(websocket_resource_url)
    ws_client.run()
