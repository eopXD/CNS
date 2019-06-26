def integer_slot_collisions():
    i = 1073741824
    perturb = i
    for x in xrange(40000):
        i = ((i << 2) + i + perturb + 1) & 0x000000000fffffff
        assert( i <= 2**30)
        print i
        perturb >>= 5

    i = 1*(2**30 - 1) + 1
    for x in xrange(10000):
        assert( i <= 2**30)
        print i
print 50000
integer_slot_collisions()
