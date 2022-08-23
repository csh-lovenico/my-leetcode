from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:

    def serialize(self, root: Optional['TreeNode']) -> str:
        """Encodes a tree to a single string.

        type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ""
        result = []
        queue = []
        result.append(str(root.val))
        queue.append([root.left, 1])
        queue.append([root.right, 1])
        current_depth = 1
        current_result = []
        while len(queue) > 0:
            head = queue.pop(0)
            if head[0] is None:
                current_result.append("null")
                continue
            if head[1] > current_depth:
                result.extend(current_result)
                current_result = []
                current_depth = head[1]
            current_result.append(str(head[0].val))
            queue.append([head[0].left, head[1] + 1])
            queue.append([head[0].right, head[1] + 1])

        if len(current_result) > 0:
            result.extend(current_result)
        return ','.join(result)

    def deserialize(self, data: str) -> Optional['TreeNode']:
        """Decodes your encoded data to tree.

        type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None
        node_list = data.split(',')
        queue = []
        init_node = TreeNode(int(node_list[0]))
        node_list.pop(0)
        queue.append(init_node)
        while queue:
            current_root = queue.pop(0)
            left_str = node_list.pop(0)
            if left_str != 'null':
                left_node = TreeNode(int(left_str))
                current_root.left = left_node
                queue.append(left_node)
            right_str = node_list.pop(0)
            if right_str != 'null':
                right_node = TreeNode(int(right_str))
                current_root.right = right_node
                queue.append(right_node)
        return init_node


if __name__ == '__main__':
    r = TreeNode(1)
    r.left = TreeNode(2)
    r.right = TreeNode(3)
    r.right.left = TreeNode(4)
    r.right.right = TreeNode(5)
    codec = Codec()
    s = codec.serialize(r)
    print(s)
    r0 = codec.deserialize(s)
    s0 = codec.serialize(r0)
    print(s0)
