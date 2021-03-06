# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    106_construct_binary_tree_from_inorder_an          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <kcheung@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/01/30 23:44:26 by kcheung           #+#    #+#              #
#    Updated: 2018/01/31 16:08:02 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

'''
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7

'''

# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def buildTreeRecur2(self, inorder, postorder, lookup,  inorder_start, inorder_end):
		if inorder_start > inorder_end:
			return None
		node = TreeNode(postorder[self.pIndex])
		inorderIndex = lookup[postorder[self.pIndex]] #find index of this node in Inorder
		self.pIndex -= 1
		if inorder_start == inorder_end:
			return node
		node.right = self.buildTreeRecur2(inorder, postorder, lookup, inorderIndex+1, inorder_end)
		node.left = self.buildTreeRecur2(inorder, postorder, lookup, inorder_start, inorderIndex-1)
		return node

	def buildTree(self, inorder, postorder):
		"""
		:type inorder: List[int]
		:type postorder: List[int]
		:rtype: TreeNode
		"""
		n = len(inorder)
		self.pIndex = n - 1
		lookup = {}
		for i,val in enumerate(inorder):
			lookup[val] = i
		return(self.buildTreeRecur2(inorder, postorder,lookup, 0, n - 1))


def printInorder(root):
	if root is None:
		return
	printInorder(root.left)
	print(root.val, end=" ")
	printInorder(root.right)

def printPostorder(root):
	if root is None:
		return
	printPostorder(root.left)
	printPostorder(root.right)
	print(root.val, end=" ")

s = Solution()
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
tree = s.buildTree(inorder, postorder)
printInorder(tree)
print()
printPostorder(tree)

