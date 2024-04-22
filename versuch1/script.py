import numpy as np
import matplotlib.pyplot as plt



def read_data(file_path):
    # Read data from file
    data = np.genfromtxt(file_path, delimiter=';', skip_header=1000, usecols=(0, 1), encoding='utf-8')

    # Convert comma-separated numbers to floats
    for i in range(len(data)):
        data[i, 0] = float(data[i, 0].replace(',', '.'))
        data[i, 1] = float(data[i, 1].replace(',', '.'))

    return data

def calculate_statistics(data):
    # Calculate mean and standard deviation
    mean = np.mean(data[:, 1])
    std_dev = np.std(data[:, 1])

    return mean, std_dev

def plot_data(data):
    plt.plot(data[:, 0], data[:, 1])
    plt.xlabel('Zeit [ms]')
    plt.ylabel('Kanal A [V]')
    plt.show()

def main():
    file_path = 'DINA4b.csv'
    data = read_data(file_path)
    #plot_data(data)
    mean, std_dev = calculate_statistics(data)
    print("Mean:", mean)
    print("Standard Deviation:", std_dev)

if __name__ == '__main__':
    main()
