import pandas as pd

class Node:
	def __init__(self, left, label, right):
		self.left = left
		self.label = label
		self.right = right
	def labels(self):
		if self.left is None:
			left_labels = set()
		else:
			left_labels = self.left.labels()
		if self.right is None:
			right_labels = set()
		else:
			right_labels = self.right.labels()
		return left_labels | {self.label} | right_labels
	def distance_between(self, label1, label2):
		if label1 == label2:
			return 0
		if self.left is not None and {label1, label2} <= self.left.labels():
			return self.left.distance_between(label1, label2)
		if self.right is not None and {label1, label2} <= self.right.labels():
			return self.right.distance_between(label1, label2)
		return self.distance_from(label1) + self.distance_from(label2)
	def distance_from(self, label):
		if label == self.label:
			return 0
		if self.left is not None and label in self.left.labels():
			return 1 + self.left.distance_from(label)
		if self.right is not None and label in self.right.labels():
			return 1 + self.right.distance_from(label)
		raise Exception(f"{label} isn't in the tree")
	def __repr__(self):
		return f"({"" if self.left is None else str(self.left)} {self.label} {"" if self.right is None else str(self.right)})"


labels = [
	"en", "sv", "da", "de", "nl", # Germanic
	"ro", "fr", "it", "es", "pt", # Romance
    "lv", "lt", # Baltic
    "pl", "sk", "cs", "sl", "bg", # Slavic
]
rabinovich_tree = Node(
	Node(
		Node(
			Node(None, "it", None),
			None,
			Node(
				Node(None, "fr", None),
				None,
				Node(None, "es", None)
			)
		),
		None,
		Node(
			Node(
				Node(None, "de", None),
				None,
				Node(None, "nl", None)
			),
			None,
			Node(
				Node(None, "en", None),
				None,
				Node(
					Node(None, "sv", None),
					None,
					Node(None, "da", None)
				)
			)
		)
	),
	None,
	Node(
		Node(
			Node(None, "ro", None),
			None,
			Node(None, "lt", None)
		),
		None,
		Node(
			Node(
				Node(None, "pt", None),
				None,
				Node(
					Node(None, "cs", None),
					None,
					Node(None, "sk", None)
				)
			),
			None,
			Node(
				Node(None, "bg", None),
				None,
				Node(
					Node(None, "lv", None),
					None,
					Node(
						Node(None, "pl", None),
						None,
						Node(None, "sl", None)
					)
				)
			)
		)
	)
)
df = pd.DataFrame([[rabinovich_tree.distance_between(l1, l2) for l2 in labels] for l1 in labels], index=labels, columns=labels)
print(df)
df.to_pickle("rabinovich_edge_distances.pkl")