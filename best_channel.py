import re
import subprocess

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def get_data():
    """Returns Available Networks"""

    available_networks = subprocess.check_output('netsh wlan show network mode=bssid',
                                                 stderr=subprocess.STDOUT,
                                                 universal_newlines=True,
                                                 shell=True)
    return available_networks


def format_data(data):
    """Formats the data"""
    parsed_text = {}

    for line in data.split('\n'):
        dict_key = ''
        dict_item = ''
        temp = {}  # Temporary dictionary that will be added to parsed_text

        line = line.replace(' ', '')  # Removes all whitespace from data

        if 'BSSID' in line:
            # Looks for BSSID2 or greater
            try:
                bssid = re.search('BSSID[2-9]', line).group(0)

                if bssid in line:
                    bssid_end = int(bssid[-1])-1
                    for i in range(bssid_end):
                        # appends networks that take up 2 channels
                        parsed_text['SSID'].append(parsed_text['SSID'][-1])
            except AttributeError:
                continue
        elif 'SSID' in line:
            ssid = line.split(':')[1]
            dict_key = 'SSID'
            dict_item = ssid
            temp[dict_key] = dict_item
        elif ':' in line:
            dict_key = line.split(':')[0]
            dict_item = line.split(':')[1]
            temp[dict_key] = dict_item

        # Checks if dict_key already exists.
        # If it does, we append to the already existing key.
        # If not, we create update it to the dictionary.
        if dict_key in parsed_text:
            parsed_text[dict_key].append(dict_item)
        else:
            temp[dict_key] = []
            temp[dict_key].append(dict_item)
            parsed_text.update(temp)

    return parsed_text


def plot_network(data_dict):

    # Remove useless keys
    data_dict.pop('', None)
    data_dict.pop('Interfacename', None)

    # creates a subset of data_dict with only SSID and Channel
    data = {key: data_dict[key] for key in ('SSID', 'Channel')}

    df = pd.DataFrame(data)
    df.where(df == '', 'Unknown')
    print(df)

    sns.countplot(df.Channel)
    plt.show()


if __name__ == '__main__':
    wifi_data = get_data()
    wifi_data_dict = format_data(wifi_data)
    print(wifi_data)
    plot_network(wifi_data_dict)
