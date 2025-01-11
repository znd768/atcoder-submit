from dataclasses import dataclass

@dataclass
class Sheet:
    height: int
    width: int
    layout: list[str]
    num_of_black: int = 0

if __name__ == '__main__':
    ha, wa = map(int, input().split())
    a: Sheet = Sheet(ha, wa, [input() for _ in range(ha)])
    hb, wb = map(int, input().split())
    b: Sheet = Sheet(hb, wb, [input() for _ in range(hb)])
    hx, wx = map(int, input().split())
    x: Sheet = Sheet(hx, wx, [input() for _ in range(hx)])

    for row in a.layout:
        a.num_of_black += row.count('#')
    for row in b.layout:
        b.num_of_black += row.count('#')

    y: Sheet = Sheet(hx, wx, ["."*wx for _ in range(hx)])

    for offset_a_h in range(-a.height, x.height):
        for offset_a_w in range(-a.width, x.width):
            for offset_b_h in range(-b.height, x.height):
                for offset_b_w in range(-b.width, x.width):
                    pass