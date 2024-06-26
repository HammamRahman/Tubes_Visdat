# -*- coding: utf-8 -*-
"""TubesVisdat.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RXnJzsPXB4AtRND1box55UGuQeZx2gjC
"""

# Import Library
import pandas as pd
from bokeh.io import output_notebook, output_file
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, HoverTool, TabPanel, Tabs
from bokeh.transform import cumsum
from bokeh.layouts import gridplot
from math import pi

# Mengatur output untuk ditampilkan di notebook
output_notebook()

# Membaca file CSV 'Data_Tanaman_Padi_Sumatera.csv' dan mengonversi kolom 'Tahun' menjadi tipe datetime
data = pd.read_csv('Data_Tanaman_Padi_Sumatera.csv', parse_dates=['Tahun'])
data

"""###Line Chart

Curah Hujan
"""

# Menyaring data, memilih kolom tertentu, dan mengurutkan data
condition = (data['Provinsi'] == 'Aceh') | (data['Provinsi'] == 'Lampung')
curah_hujan = data[condition]
curah_hujan = curah_hujan.loc[:, ['Tahun', 'Provinsi', 'Curahhujan']]
curah_hujan = curah_hujan.sort_values(['Provinsi', 'Tahun'])

# Memisahkan data curah hujan untuk provinsi Aceh dan Lampung
aceh_data = curah_hujan[curah_hujan['Provinsi'] == 'Aceh']
lampung_data = curah_hujan[curah_hujan['Provinsi'] == 'Lampung']

# Membuat ColumnDataSource untuk data Aceh dan Lampung
aceh_cds = ColumnDataSource(aceh_data)
lampung_cds = ColumnDataSource(lampung_data)

# Membuat plot untuk visualisasi curah hujan
curah_hujan_fig = figure(x_axis_type='datetime',
             height=600, width=800,
             title='Perbandingan Curah Hujan Aceh dan Lampung',
             x_axis_label='Year', y_axis_label='Curah Hujan')

# Menambahkan hovertool untuk menampilkan informasi tambahan saat kursor melayang di atas titik data
hover = HoverTool(tooltips=[("Provinsi", "@Provinsi"),("Curahhujan", "@Curahhujan")])
curah_hujan_fig.add_tools(hover)

# Menambahkan line plot untuk data curah hujan Aceh dan Lampung
curah_hujan_fig.line('Tahun', 'Curahhujan',
            color='#CE1141', legend_label='Aceh',
            source=aceh_cds)
curah_hujan_fig.line('Tahun', 'Curahhujan',
            color='#006BB6', legend_label='Lampung',
            source=lampung_cds)

# Menambahkan scatter plot untuk data curah hujan Aceh dan Lampung
curah_hujan_fig.scatter('Tahun', 'Curahhujan',
              color='#007A33', legend_label='Aceh',
              source=aceh_cds )
curah_hujan_fig.scatter('Tahun', 'Curahhujan',
              color='#CE1141', legend_label='Lampung',
              source=lampung_cds)

# Mengatur lokasi legenda di pojok kanan atas
curah_hujan_fig.legend.location = 'top_right'

# Menampilkan plot
show(curah_hujan_fig)

"""Kelembapan"""

# Menyaring data, memilih kolom tertentu, dan mengurutkan data
condition = (data['Provinsi'] == 'Aceh') | (data['Provinsi'] == 'Lampung')
kelembapan = data[condition]
kelembapan = kelembapan.loc[:, ['Tahun', 'Provinsi', 'Kelembapan']]
kelembapan = kelembapan.sort_values(['Provinsi', 'Tahun'])

# Memisahkan data kelembapan untuk provinsi Aceh dan Lampung
aceh_data = kelembapan[kelembapan['Provinsi'] == 'Aceh']
lampung_data = kelembapan[kelembapan['Provinsi'] == 'Lampung']

# Membuat ColumnDataSource untuk data Aceh dan Lampung
aceh_cds = ColumnDataSource(aceh_data)
lampung_cds = ColumnDataSource(lampung_data)

# Membuat plot untuk visualisasi kelembapan dengan tipe sumbu x 'datetime'
kelembapan_fig = figure(x_axis_type='datetime',
             height=600, width=800,
             title='Perbandingan Kelembapan Aceh dan Lampung',
             x_axis_label='Year', y_axis_label='Kelembapan')

# Menambahkan hovertool untuk menampilkan informasi tambahan saat kursor melayang di atas titik data
hover = HoverTool(tooltips=[("Provinsi", "@Provinsi"),("Kelembapan", "@Kelembapan")])
kelembapan_fig.add_tools(hover)

# Menambahkan line plot untuk data kelembapan Aceh dan Lampung
kelembapan_fig.line('Tahun', 'Kelembapan',
            color='#CE1141', legend_label='Aceh',
            source=aceh_cds)
kelembapan_fig.line('Tahun', 'Kelembapan',
            color='#006BB6', legend_label='Lampung',
            source=lampung_cds)

# Menambahkan scatter plot untuk data kelembapan Aceh dan Lampung
kelembapan_fig.scatter('Tahun', 'Kelembapan',
              color='#007A33', legend_label='Aceh',
              source=aceh_cds )
kelembapan_fig.scatter('Tahun', 'Kelembapan',
              color='#CE1141', legend_label='Lampung',
              source=lampung_cds)

# Mengatur lokasi legenda di pojok kanan atas
kelembapan_fig.legend.location = 'top_right'

# Menampilkan plot
show(kelembapan_fig)

"""Suhu Rata Rata"""

# Menyaring data, memilih kolom tertentu, dan mengurutkan data
condition = (data['Provinsi'] == 'Aceh') | (data['Provinsi'] == 'Lampung')
suhu = data[condition]
suhu = suhu.loc[:, ['Tahun', 'Provinsi', 'Suhuratarata']]
suhu = suhu.sort_values(['Provinsi', 'Tahun'])

# Memisahkan data suhu rata rata untuk provinsi Aceh dan Lampung
aceh_data = suhu[suhu['Provinsi'] == 'Aceh']
lampung_data = suhu[suhu['Provinsi'] == 'Lampung']

# Membuat ColumnDataSource untuk data Aceh dan Lampung
aceh_cds = ColumnDataSource(aceh_data)
lampung_cds = ColumnDataSource(lampung_data)

# Membuat plot untuk visualisasi suhu rata rata dengan tipe sumbu x 'datetime'
suhu_fig = figure(x_axis_type='datetime',
             height=600, width=800,
             title='Perbandingan Suhu Rata-Rata Aceh dan Lampung',
             x_axis_label='Year', y_axis_label='Suhu Rata-Rata')

# Menambahkan hovertool untuk menampilkan informasi tambahan saat kursor melayang di atas titik data
hover = HoverTool(tooltips=[("Provinsi", "@Provinsi"),("Suhu Rata-Rata", "@Suhuratarata")])
suhu_fig.add_tools(hover)

# Menambahkan line plot untuk data suhu rata rata Aceh dan Lampung
suhu_fig.line('Tahun', 'Suhuratarata',
            color='#CE1141', legend_label='Aceh',
            source=aceh_cds)
suhu_fig.line('Tahun', 'Suhuratarata',
            color='#006BB6', legend_label='Lampung',
            source=lampung_cds)

# Menambahkan scatter plot untuk data suhu rata rata Aceh dan Lampung
suhu_fig.scatter('Tahun', 'Suhuratarata',
              color='#007A33', legend_label='Aceh',
              source=aceh_cds )
suhu_fig.scatter('Tahun', 'Suhuratarata',
              color='#CE1141', legend_label='Lampung',
              source=lampung_cds)

# Mengatur lokasi legenda di pojok kanan atas
suhu_fig.legend.location = 'top_right'

# Menampilkan plot
show(suhu_fig)

"""###Pie Chart

Curah Hujan
"""

# Persiapan data
condition = (data['Provinsi'] == 'Aceh') | (data['Provinsi'] == 'Lampung')
curah_hujan = data[condition]
curah_hujan = curah_hujan.loc[:, ['Provinsi', 'Curahhujan']]

# Menghitung total curah hujan per provinsi
total_curah_hujan = curah_hujan.groupby('Provinsi').sum().reset_index()
total_curah_hujan.columns = ['Provinsi', 'TotalCurahHujan']

# Menambahkan kolom persentase dan sudut pie chart
total_curah_hujan['Percentage'] = total_curah_hujan['TotalCurahHujan'] / total_curah_hujan['TotalCurahHujan'].sum() * 100
total_curah_hujan['Angle'] = total_curah_hujan['TotalCurahHujan'] / total_curah_hujan['TotalCurahHujan'].sum() * 2 * pi
total_curah_hujan['Color'] = ['#CE1141', '#006BB6']  # Warna untuk Aceh dan Lampung

# ColumnDataSource untuk pie chart
source = ColumnDataSource(total_curah_hujan)

# Membuat plot untuk visualisasi pie chart curah hujan
pie_chart_c = figure(height=600, width=800, title="Pie Chart Curah Hujan Aceh dan Lampung",
                   toolbar_location=None, tools="hover", tooltips="@Provinsi: @Percentage{0.2f}%", x_range=(-0.5, 1.0))

pie_chart_c.wedge(x=0, y=1, radius=0.4,
                start_angle=cumsum('Angle', include_zero=True), end_angle=cumsum('Angle'),
                line_color="white", fill_color='Color', legend_field='Provinsi', source=source)

# Menampilkan plot
show(pie_chart_c)

"""Kelembapan"""

# Persiapan data
condition = (data['Provinsi'] == 'Aceh') | (data['Provinsi'] == 'Lampung')
kelembapan = data[condition]
kelembapan = kelembapan.loc[:, ['Provinsi', 'Kelembapan']]

# Menghitung total curah hujan per provinsi
total_kelembapan = kelembapan.groupby('Provinsi').sum().reset_index()
total_kelembapan.columns = ['Provinsi', 'TotalKelembapan']

# Menambahkan kolom persentase dan sudut pie chart
total_kelembapan['Percentage'] = total_kelembapan['TotalKelembapan'] / total_kelembapan['TotalKelembapan'].sum() * 100
total_kelembapan['Angle'] = total_kelembapan['TotalKelembapan'] / total_kelembapan['TotalKelembapan'].sum() * 2 * pi
total_kelembapan['Color'] = ['#CE1141', '#006BB6']  # Warna untuk Aceh dan Lampung

# ColumnDataSource untuk pie chart
source = ColumnDataSource(total_kelembapan)

# Membuat plot untuk visualisasi pie chart kelembapan
pie_chart_k = figure(height=600, width=800, title="Pie Chart Kelembapan Aceh dan Lampung",
                   toolbar_location=None, tools="hover", tooltips="@Provinsi: @Percentage{0.2f}%", x_range=(-0.5, 1.0))

pie_chart_k.wedge(x=0, y=1, radius=0.4,
                start_angle=cumsum('Angle', include_zero=True), end_angle=cumsum('Angle'),
                line_color="white", fill_color='Color', legend_field='Provinsi', source=source)

# Menampilkan plot
show(pie_chart_k)

"""Suhu Rata Rata"""

# Asumsikan 'data' adalah DataFrame yang sudah ada

# Persiapan data
condition = (data['Provinsi'] == 'Aceh') | (data['Provinsi'] == 'Lampung')
suhu = data[condition]
suhu = suhu.loc[:, ['Provinsi', 'Suhuratarata']]

# Menghitung total suhu rata-rata per provinsi
total_suhu = suhu.groupby('Provinsi').sum().reset_index()
total_suhu.columns = ['Provinsi', 'TotalSuhu']

# Menambahkan kolom persentase dan sudut pie chart
total_suhu['Percentage'] = total_suhu['TotalSuhu'] / total_suhu['TotalSuhu'].sum() * 100
total_suhu['Angle'] = total_suhu['TotalSuhu'] / total_suhu['TotalSuhu'].sum() * 2 * pi
total_suhu['Color'] = ['#CE1141', '#006BB6']  # Warna untuk Aceh dan Lampung

# ColumnDataSource untuk pie chart
source = ColumnDataSource(total_suhu)

# Membuat plot untuk visualisasi pie chart suhu rata rata
pie_chart_s = figure(height=600, width=800, title="Pie Chart Suhu Rata-Rata Aceh dan Lampung",
                   toolbar_location=None, tools="hover", tooltips="@Provinsi: @Percentage{0.2f}%", x_range=(-0.5, 1.0))

pie_chart_s.wedge(x=0, y=1, radius=0.4,
                start_angle=cumsum('Angle', include_zero=True), end_angle=cumsum('Angle'),
                line_color="white", fill_color='Color', legend_field='Provinsi', source=source)

# Menampilkan plot
show(pie_chart_s)

"""###GridPlot

Curah Hujan
"""

# Membuat grid plot dengan dua plot, 'curah_hujan_fig' dan 'pie_chart_c'
c_gridplot = gridplot([[curah_hujan_fig, pie_chart_c]],
                              toolbar_location='right')

# Menampilkan grid plot
show(c_gridplot)

"""Kelembapan"""

# Membuat gridplot yang berisi dua plot, 'kelembapan_fig' dan 'pie_chart_k'
k_gridplot = gridplot([[kelembapan_fig, pie_chart_k]],
                              toolbar_location='right')

# Menampilkan grid plot yang telah dibuat
show(k_gridplot)

"""Suhu Rata-Rata

"""

# Membuat gridplot yang berisi dua plot, 'suhu_fig' dan 'pie_chart_s'
s_gridplot = gridplot([[suhu_fig, pie_chart_s]],
                              toolbar_location='right')

# Menampilkan grid plot yang telah dibuat
show(s_gridplot)

"""###Hasil"""

# File output
output_file('Aceh dan Lampung.html',
            title='Perbandingan Cuaca Aceh dan Lampung')


# Membuat 3 panel, curah hujan, kelembapan, dan suhu rata rata
c_panel = TabPanel(child=c_gridplot, title='Curah Hujan')
k_panel = TabPanel(child=k_gridplot, title='Kelembapan')
s_panel = TabPanel(child=s_gridplot, title='Suhu Rata-Rata')

# Menambahkan panel kedalam tabs
tabs = Tabs(tabs=[c_panel, k_panel, s_panel])

# Menampilkan tabs
show(tabs)