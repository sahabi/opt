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
    def move(self,i1, i2, i3, i4, o1, o2, o3):
        tmp3 = evaluate(o1, True, False);
        tmp5 = evaluate(i4, True, tmp3);
        tmp4 = evaluate(i3, tmp5, tmp3);
        tmp2 = evaluate(i2, tmp3, tmp4);
        tmp8 = evaluate(i4, tmp3, False);
        tmp7 = evaluate(i3, tmp3, tmp8);
        tmp9 = evaluate(i3, tmp8, tmp5);
        tmp6 = evaluate(i2, tmp7, tmp9);
        tmp1 = evaluate(i1, tmp2, tmp6);
        o1__1 = tmp1;

        tmp13 = evaluate(o2, True, False);
        tmp15 = evaluate(o1, True, False);
        tmp14 = evaluate(i4, tmp13, tmp15);
        tmp12 = evaluate(i3, tmp13, tmp14);
        tmp18 = inv_evaluate(o1, True, False);
        tmp17 = evaluate(i4, tmp13, tmp18);
        tmp19 = evaluate(i4, tmp15, tmp13);
        tmp16 = evaluate(i3, tmp17, tmp19);
        tmp11 = evaluate(i2, tmp12, tmp16);
        tmp23 = inv_evaluate(o2, True, False);
        tmp22 = evaluate(i4, tmp15, tmp23);
        tmp21 = inv_evaluate(i3, tmp22, tmp23);
        tmp20 = evaluate(i2, tmp13, tmp21);
        tmp10 = evaluate(i1, tmp11, tmp20);
        o2__1 = tmp10;

        tmp27 = evaluate(o3, True, False);
        tmp29 = evaluate(o1, tmp27, False);
        tmp28 = evaluate(i4, tmp27, tmp29);
        tmp26 = evaluate(i3, tmp27, tmp28);
        tmp34 = inv_evaluate(o3, True, False);
        tmp33 = evaluate(o2, True, tmp34);
        tmp32 = evaluate(o1, tmp33, True);
        tmp35 = evaluate(o1, True, tmp34);
        tmp31 = evaluate(i4, tmp32, tmp35);
        tmp36 = inv_evaluate(i4, tmp29, tmp27);
        tmp30 = inv_evaluate(i3, tmp31, tmp36);
        tmp25 = evaluate(i2, tmp26, tmp30);
        tmp40 = inv_evaluate(o1, True, tmp33);
        tmp39 = evaluate(i4, tmp27, tmp40);
        tmp38 = evaluate(i3, tmp27, tmp39);
        tmp43 = evaluate(o1, True, tmp33);
        tmp42 = evaluate(i4, tmp35, tmp43);
        tmp44 = evaluate(i4, tmp32, tmp34);
        tmp41 = inv_evaluate(i3, tmp42, tmp44);
        tmp37 = evaluate(i2, tmp38, tmp41);
        tmp24 = evaluate(i1, tmp25, tmp37);
        o3__1 = tmp24;

        self.s0 = False;

        return (o1__1, o2__1, o3__1)