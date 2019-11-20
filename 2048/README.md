# 2048

It is a simple implementation for 2048 game compatible in python 2.7


### Sample Usage
```python
if __name__ == '__main__':
    # dim - dimension of board
    # target - Target to be achieved, assumed to be of order 2^n
    # display - to display the board for every move
    game = Game(dim=4, target=2048, display=True)
    while True:
        k = get_key()
        game.shift(k)
```

### How to play

```python
>> python 2048.py
[[0 0 0 0]
 [2 0 0 0]
 [0 2 0 0]
 [0 0 0 0]]
```
And use arrows to play.

To terminate, press any keys except arrow keys.