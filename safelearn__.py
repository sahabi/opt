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
    def move(self,i1, i2, i3, o1, o2, o3):
        tmp2 = evaluate(o1, True, False);
        tmp4 = evaluate(i3, tmp2, False);
        tmp5 = evaluate(i3, True, tmp2);
        tmp3 = evaluate(i2, tmp4, tmp5);
        tmp1 = evaluate(i1, tmp2, tmp3);
        o1__1 = tmp1;

        tmp8 = evaluate(o2, True, False);
        tmp10 = evaluate(o1, True, False);
        tmp9 = evaluate(i3, tmp8, tmp10);
        tmp7 = evaluate(i2, tmp8, tmp9);
        tmp12 = evaluate(i3, tmp10, False);
        tmp13 = inv_evaluate(o2, True, False);
        tmp11 = inv_evaluate(i2, tmp12, tmp13);
        tmp6 = evaluate(i1, tmp7, tmp11);
        o2__1 = tmp6;

        tmp16 = evaluate(o3, True, False);
        tmp18 = evaluate(o1, True, tmp16);
        tmp17 = evaluate(i3, tmp16, tmp18);
        tmp15 = evaluate(i2, tmp16, tmp17);
        tmp21 = evaluate(o1, tmp16, True);
        tmp20 = evaluate(i3, tmp21, tmp16);
        tmp23 = evaluate(o2, True, False);
        tmp24 = inv_evaluate(o3, True, False);
        tmp22 = inv_evaluate(i3, tmp23, tmp24);
        tmp19 = evaluate(i2, tmp20, tmp22);
        tmp14 = evaluate(i1, tmp15, tmp19);
        o3__1 = tmp14;

        self.s0 = False;

        return (o1__1, o2__1, o3__1)