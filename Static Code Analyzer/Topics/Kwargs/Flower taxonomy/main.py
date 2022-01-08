iris = {}


def add_iris(id_n, species, petal_length, petal_width, **additional):
    global iris
    iris.update({
        id_n: {
            'species': species,
            'petal_length': petal_length,
            'petal_width': petal_width,
        },
    })
    iris[id_n].update(additional)
