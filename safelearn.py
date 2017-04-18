def evaluate(operand, a, b):
    if operand:
        return a
    else:
        return b

def inv_evaluate(operand, a, b):
    if operand:
        return not a
    else:
        return not b 


class Shield(object):
    def __init__(self):
        self.s0 = False;
    def move(self,i3, i2, i1, o3, o2, o1):
        tmp1 = evaluate(o1, True, False);
        o1__1 = tmp1;

        tmp2 = evaluate(o2, True, False);
        o2__1 = tmp2;

        tmp6 = evaluate(o3, True, False);
        tmp8 = evaluate(o2, True, False);
        tmp9 = inv_evaluate(o2, tmp6, True);
        tmp7 = inv_evaluate(o1, tmp8, tmp9);
        tmp5 = evaluate(i3, tmp6, tmp7);
        tmp12 = evaluate(o2, True, tmp6);
        tmp11 = evaluate(o1, True, tmp12);
        tmp10 = evaluate(i3, tmp6, tmp11);
        tmp4 = evaluate(i2, tmp5, tmp10);
        tmp17 = inv_evaluate(o3, True, False);
        tmp16 = evaluate(o2, True, tmp17);
        tmp15 = inv_evaluate(o1, True, tmp16);
        tmp14 = evaluate(i3, tmp6, tmp15);
        tmp20 = evaluate(o2, tmp6, False);
        tmp19 = evaluate(o1, tmp8, tmp20);
        tmp18 = evaluate(i3, tmp19, tmp6);
        tmp13 = evaluate(i2, tmp14, tmp18);
        tmp3 = evaluate(i1, tmp4, tmp13);
        o3__1 = tmp3;

        self.s0 = False;

        return (o3__1, o2__1, o1__1)