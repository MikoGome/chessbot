def initialize():
    board = [
        {
          "pos": "a8",
          "coord": [313, 66]
        },
        {
          "pos": "b8",
          "coord": [427, 66]
        },
        {
          "pos": "c8",
          "coord": [549, 66]
        },
        {
          "pos": "d8",
          "coord": [667, 66]
        },
        {
          "pos": "e8",
          "coord": [783, 66]
        },
        {
          "pos": "f8",
          "coord": [900, 66]
        },
        {
          "pos": "g8",
          "coord": [1018, 66]
        },
        {
          "pos": "h8",
          "coord": [1139, 66]
        },


        {
          "pos": "a7",
          "coord": [313, 191]
        },
        {
          "pos": "b7",
          "coord": [427, 191]
        },
        {
          "pos": "c7",
          "coord": [549, 191]
        },
        {
          "pos": "d7",
          "coord": [667, 191]
        },
        {
          "pos": "e7",
          "coord": [783, 191]
        },
        {
          "pos": "f7",
          "coord": [900, 191]
        },
        {
          "pos": "g7",
          "coord": [1018, 191]
        },
        {
          "pos": "h7",
          "coord": [1139, 191]
        },


        {
          "pos": "a6",
          "coord": [313, 306]
        },
        {
          "pos": "b6",
          "coord": [427, 306]
        },
        {
          "pos": "c6",
          "coord": [549, 306]
        },
        {
          "pos": "d6",
          "coord": [667, 306]
        },
        {
          "pos": "e6",
          "coord": [783, 306]
        },
        {
          "pos": "f6",
          "coord": [900, 306]
        },
        {
          "pos": "g6",
          "coord": [1018, 306]
        },
        {
          "pos": "h6",
          "coord": [1139, 306]
        },


        {
          "pos": "a5",
          "coord": [313, 426]
        },
        {
          "pos": "b5",
          "coord": [427, 426]
        },
        {
          "pos": "c5",
          "coord": [549, 426]
        },
        {
          "pos": "d5",
          "coord": [667, 426]
        },
        {
          "pos": "e5",
          "coord": [783, 426]
        },
        {
          "pos": "f5",
          "coord": [900, 426]
        },
        {
          "pos": "g5",
          "coord": [1018, 426]
        },
        {
          "pos": "h5",
          "coord": [1139, 426]
        },


        {
          "pos": "a4",
          "coord": [313, 541]
        },
        {
          "pos": "b4",
          "coord": [427, 541]
        },
        {
          "pos": "c4",
          "coord": [549, 541]
        },
        {
          "pos": "d4",
          "coord": [667, 541]
        },
        {
          "pos": "e4",
          "coord": [783, 541]
        },
        {
          "pos": "f4",
          "coord": [900, 541]
        },
        {
          "pos": "g4",
          "coord": [1018, 541]
        },
        {
          "pos": "h4",
          "coord": [1139, 541]
        },


        {
          "pos": "a3",
          "coord": [313, 660]
        },
        {
          "pos": "b3",
          "coord": [427, 660]
        },
        {
          "pos": "c3",
          "coord": [549, 660]
        },
        {
          "pos": "d3",
          "coord": [667, 660]
        },
        {
          "pos": "e3",
          "coord": [783, 660]
        },
        {
          "pos": "f3",
          "coord": [900, 660]
        },
        {
          "pos": "g3",
          "coord": [1018, 660]
        },
        {
          "pos": "h3",
          "coord": [1139, 660]
        },

        {
          "pos": "a2",
          "coord": [313, 779]
        },
        {
          "pos": "b2",
          "coord": [427, 779]
        },
        {
          "pos": "c2",
          "coord": [549, 779]
        },
        {
          "pos": "d2",
          "coord": [667, 779]
        },
        {
          "pos": "e2",
          "coord": [783, 779]
        },
        {
          "pos": "f2",
          "coord": [900, 779]
        },
        {
          "pos": "g2",
          "coord": [1018, 779]
        },
        {
          "pos": "h2",
          "coord": [1139, 779]
        },


        {
          "pos": "a1",
          "coord": [313, 896]
        },
        {
          "pos": "b1",
          "coord": [427, 896]
        },
        {
          "pos": "c1",
          "coord": [549, 896]
        },
        {
          "pos": "d1",
          "coord": [667, 896]
        },
        {
          "pos": "e1",
          "coord": [783, 896]
        },
        {
          "pos": "f1",
          "coord": [900, 896]
        },
        {
          "pos": "g1",
          "coord": [1018, 896]
        },
        {
          "pos": "h1",
          "coord": [1139, 896]
        }, 
    ]
    return board

def flip(lst):
    #a8 -> h1
    letters="abcdefgh"
    numbers = "12345678"
    for square in lst:
        initial_pos = square["pos"]
        letter = letters[len(letters) - 1 - letters.index(initial_pos[0])]
        number = numbers[len(numbers) - 1 - numbers.index(initial_pos[1])]
        square["pos"] = letter+number

