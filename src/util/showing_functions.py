def show_sorted_traversal(traversal):
    for key in sorted(traversal.keys()):
        print ("%s : %s" % (key, traversal[key]))
