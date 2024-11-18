def repair_tree(tree):
    global step

    root = preorder[step]
    idx = tree.index(root)
    left = tree[:idx]
    right = []
    if idx != len(tree):
        right = tree[idx+1:]

    if left:
        step += 1
        repair_tree(left)
    if right:
        step += 1
        repair_tree(right)
    print(root,end='')

while True:
    preorder,inorder = '',''
    try:
        preorder,inorder = input().split()
    except:
        break

    step = 0
    repair_tree(inorder)
    print('')