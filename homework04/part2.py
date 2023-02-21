from math import sqrt

from flask import Flask
from xml.dom.minidom import parse
import xml.dom.minidom

app = Flask(__name__)


@app.route('/')
def data_set():
    """
    Return the entire data set
    :return: the entire data set
    """
    return dic


@app.route('/epochs/')
def get_epochs():
    """
    Return a list of all Epochs in the data set
    :return: a list of all Epochs
    """
    epochs = []
    for data in dic:
        epochs.append(data['EPOCH'])
    return epochs


@app.route('/epochs/<epoch>/')
def get_epoch_data(epoch: str):
    """
    Return state vectors for a specific Epoch from the data set
    :param epoch: specific Epoch
    :return: state vectors
    """
    for data in dic:
        if data['EPOCH'] == epoch:
            res = data.copy()
            res.pop('EPOCH')
            return res


@app.route('/epochs/<epoch>/speed')
def get_epoch_speed(epoch: str):
    """
    Return instantaneous speed for a specific Epoch in the data set
    :param epoch: specific Epoch
    :return: instantaneous speed
    """
    for data in dic:
        print(data)
        if data['EPOCH'] == epoch:
            res = sqrt(data['X_DOT'] ** 2 + data['Y_DOT'] ** 2 + data['Z_DOT'] ** 2)
            return str(res)


def read_file(filename: str):
    DOMTree = xml.dom.minidom.parse(filename)
    collection = DOMTree.documentElement
    vectors = collection.getElementsByTagName("stateVector")
    res = []
    for vector in vectors:
        data = {}
        EPOCH = vector.getElementsByTagName('EPOCH')[0]
        X = vector.getElementsByTagName('X')[0]
        Y = vector.getElementsByTagName('Y')[0]
        Z = vector.getElementsByTagName('Z')[0]
        X_DOT = vector.getElementsByTagName('X_DOT')[0]
        Y_DOT = vector.getElementsByTagName('Y_DOT')[0]
        Z_DOT = vector.getElementsByTagName('Z_DOT')[0]
        data['EPOCH'] = EPOCH.childNodes[0].data
        data['X'] = float(X.childNodes[0].data)
        data['Y'] = float(Y.childNodes[0].data)
        data['Z'] = float(Z.childNodes[0].data)
        data['X_DOT'] = float(X_DOT.childNodes[0].data)
        data['Y_DOT'] = float(Y_DOT.childNodes[0].data)
        data['Z_DOT'] = float(Z_DOT.childNodes[0].data)
        res.append(data)
    return res


if __name__ == '__main__':
    dic = read_file('ISS.OEM_J2K_EPH.xml')
    app.run()
