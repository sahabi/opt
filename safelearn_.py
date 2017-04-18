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
        tmp1 = evaluate(o1, True, False);
        o1__1 = tmp1;

        tmp4 = evaluate(o2, True, False);
        tmp6 = evaluate(o1, True, tmp4);
        tmp5 = evaluate(i3, tmp4, tmp6);
        tmp3 = evaluate(i2, tmp4, tmp5);
        tmp9 = evaluate(o1, tmp4, True);
        tmp11 = inv_evaluate(o2, True, False);
        tmp10 = inv_evaluate(o1, True, tmp11);
        tmp8 = evaluate(i3, tmp9, tmp10);
        tmp13 = evaluate(o1, tmp4, False);
        tmp12 = evaluate(i3, tmp13, tmp4);
        tmp7 = evaluate(i2, tmp8, tmp12);
        tmp2 = evaluate(i1, tmp3, tmp7);
        o2__1 = tmp2;

        tmp16 = evaluate(o3, True, False);
        tmp20 = inv_evaluate(o3, True, False);
        tmp19 = inv_evaluate(o2, True, tmp20);
        tmp18 = evaluate(o1, tmp16, tmp19);
        tmp17 = evaluate(i3, tmp16, tmp18);
        tmp15 = evaluate(i2, tmp16, tmp17);
        tmp24 = evaluate(o2, True, tmp20);
        tmp23 = evaluate(o1, tmp24, tmp20);
        tmp25 = evaluate(o1, True, tmp20);
        tmp22 = evaluate(i3, tmp23, tmp25);
        tmp27 = evaluate(o1, tmp16, False);
        tmp26 = inv_evaluate(i3, tmp27, tmp16);
        tmp21 = inv_evaluate(i2, tmp22, tmp26);
        tmp14 = evaluate(i1, tmp15, tmp21);
        o3__1 = tmp14;

        self.s0 = False;
        if o1 != o1__1 or o2 != o2__1 or o3 != o3__1:
            print "correction!!"

        return (o1__1, o2__1, o3__1)