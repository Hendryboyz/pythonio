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

### Unit Test

```bash
## Linux Mint require super user permission to install pytest
# sudo su
source venv/bin/activate
pip install -U pytest
pytest pythonio
```

### The Files

- server: `pythonio/key_server.py`
- client1: `pythonio/websocket_listener.py`
- client2: `pythonio/pipe_listener.py`
- client3: `pythonio/shared_memory_listener.py`
- unit test: `pythonio/test_calculate.py`

### Todo list

- [x] Client to caculate Mean
- [x] Client to caculate Median
- [x] Client to find Mode

### Future Work

- [ ] Handle client connect to server error
- [ ] Dockerfile to build a container accepting keyboard events
- [ ] Compare [keyboard](https://github.com/boppreh/keyboard) with [pynput](https://pynput.readthedocs.io/en/latest/) module to handle keyboard events
- [ ] Introduce pattern to handle calculate/connect logic in client code
