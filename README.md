## Multiple Processing(with `multiprocessing` library)

### How to Run

```bash
echo 'Setup virtual environment'
python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
```

```bash
sudo su # keyboard package require super user permission
python -m pythonio.main
```

### The Files

* server: `pythonio/key_server.py`
* client1: `pythonio/websocket_listener.py`
* client2: `pythonio/pipe_listener.py`
* client3: `pythonio/shared_memory_listener.py`

### Todo list

- [x] Client to caculate Mean
- [x] Client to caculate Median
- [ ] Client to find Mode