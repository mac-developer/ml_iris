"""Define model."""
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier


def run():
    """Run model."""
    full = load_iris()

    data = full.data[0:45] + full.data[50:95] + full.data[100:-5]
    tests = full.data[45:50] + full.data[95:100] + full.data[-5:]
    target = full.target[0:45] + full.target[50:95] + full.target[100:-5]

    nbrs = KNeighborsClassifier(n_neighbors=1)
    nbrs.fit(data, target)

    print(nbrs.predict(tests))
