import matplotlib.pyplot as plt
import dwfpy as dwf
import pandas as pd
import numpy as np
import zlib

print(f'DWF Version: {dwf.Application.get_version()}')

with dwf.AnalogDiscovery2() as device:
    print(f'Found device: {device.name} ({device.serial_number})')

    scope = device.analog_input

    print("Starting oscilloscope...")
    scope[0].setup(range=30)
    scope[1].setup(range=30)
    scope.setup_edge_trigger(
        mode='auto', channel=0, slope='rising', level=0, hysteresis=0, position=0
    )
    recorder = scope.record(sample_rate=1e6, length=10, configure=True, start=True)

    if recorder.lost_samples > 0:
        print('Samples lost, reduce sample rate.')
    if recorder.corrupted_samples > 0:
        print('Samples corrupted, reduce sample rate.')

    print(
        f'Processed {recorder.total_samples} samples total, '
        f'received {len(recorder.channels[0].data_samples)} samples.'
    )
    
print('Tamanho:' + str(len(recorder.channels[0].data_samples)))
print('Máximo:' + str(max(recorder.channels[0].data_samples)))
print('Mínimo:' + str(min(recorder.channels[0].data_samples)))
# plt.figure(figsize=(25, 5))
# plt.plot(recorder.channels[0].data_samples, linestyle='-')
# # plt.xlim(4000000, 5000000)
# plt.show()

print('Tamanho:' + str(len(recorder.channels[1].data_samples)))
print('Máximo:' + str(max(recorder.channels[1].data_samples)))
print('Mínimo:' + str(min(recorder.channels[1].data_samples)))
# plt.figure(figsize=(25, 5))
# plt.plot(recorder.channels[1].data_samples, linestyle='-')
# # plt.xlim(4000000, 5000000)
# plt.show()

data = {
    'Canal 1': recorder.channels[0].data_samples,
    'Canal 2': recorder.channels[1].data_samples,
}

df = pd.DataFrame(data)
df_np = df.to_numpy()
# df.to_csv('/home/pi/Documents/Digilent/dados_linux.csv', index=False)
print('Start')
np.save('/home/pi/Documents/Digilent/dados_linux', df_np)
print('Finish')

print('Start')
with open('/home/pi/Documents/Digilent/dados_linux_compressed.npy', 'wb') as f:
    compressed_data = zlib.compress(df_np.tobytes())
    f.write(compressed_data)
print('Finish')