def show_sorted_traversal(traversal):
    for key in sorted(traversal.keys()):
        print ("%s : %s" % (traversal[key], key))
