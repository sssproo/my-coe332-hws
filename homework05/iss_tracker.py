from math import sqrt

from flask import Flask, request
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
    offset = request.args.get("offset")
    limit = request.args.get("limit")
    print(f"epochs offset:{offset}, limit:{limit}")
    if offset and limit:
        try:
            offset = int(offset)
            limit = int(limit)
            return epochs[offset:offset+limit]
        except ValueError as e:
            return f"Exception occurred:{e}, will not send epochs for current query"
    elif offset or limit:
        return f"Not supporting single value provided, please provide both offset and limit"
    else:
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

@app.route('/help')
def help_doc():
    """
    Return the help message
    :return: the help message string
    """
    table_doc="""
    usage: http://host:port&lt;Route&gt;
    <table>
	<tbody>
		<tr>
			<td>Route</td>
			<td>Method</td>
			<td>Explain</td>
		</tr>
		<tr>
			<td>/</td>
			<td>GET</td>
			<td>Return entire data set</td>
		</tr>
		<tr>
			<td>/epochs</td>
			<td>GET</td>
			<td>Return list of all Epochs in the data set</td>
		</tr>
  		<tr>
			<td>/epochs?limit=int&offset=int</td>
			<td>GET</td>
			<td>Return modified list of Epochs given query parameters</td>
		</tr>
  		<tr>
			<td>/epochs/<epoch></td>
			<td>GET</td>
			<td>Return state vectors for a specific Epoch from the data set</td>
		</tr>
  		<tr>
			<td>/epochs/<epoch>/speed</td>
			<td>GET</td>
			<td>Return instantaneous speed for a specific Epoch in the data set</td>
		</tr>
  		<tr>
			<td>/help</td>
			<td>GET</td>
			<td>Return help text (as a string) that briefly describes each route</td>
		</tr>
  		<tr>
			<td>/delete-data</td>
			<td>DELETE</td>
			<td>Delete all data from the dictionary object</td>
		</tr>
        <tr>
			<td>/post-data</td>
			<td>POST</td>
			<td>Reload the dictionary object with data from the web</td>
		</tr>
	</tbody>
    </table>
    """
    return table_doc


@app.route('/delete-data', methods=['DELETE'])
def delete_data():
    dic.clear()
    return dic


@app.route('/post-data', methods=['POST'])
def post_data():
    dic = request.get_data(request.form)
    return dic
    

if __name__ == '__main__':
    dic = read_file('ISS.OEM_J2K_EPH.xml')
    app.run()
