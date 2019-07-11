# matrix-benchmarks

Benchmarks comparing [NumPy](https://www.numpy.org/) and
[J](https://www.jsoftware.com/#/).

## Results

As you can see, J is faster to fill a matrix and multiply it. NumPy is faster
when filling and inverting a matrix.

<table>
  <tr>
    <th>Task</th>
    <th>Language</th>
    <th>Time</th>
  </tr>
  <tr>
    <td>Matrix Multiplication</td>
    <th>J</th>
    <th>1.41s</th>
  </tr>
  <tr>
    <td>Matrix Inversion</td>
    <th>J</th>
    <th>3.87s</th>
  </tr>
  <tr>
    <td>Matrix Multiplication</td>
    <th>Python (MKL)</th>
    <th>40.1s</th>
  </tr>
  <tr>
    <td>Matrix Inversion</td>
    <th>Python (MKL)</th>
    <th>0.59s</th>
  </tr>
  <tr>
    <td>Matrix Multiplication</td>
    <th>Python (Ubuntu)</th>
    <th>18.21s</th>
  </tr>
  <tr>
    <td>Matrix Inversion</td>
    <th>Python (Ubuntu)</th>
    <th>18.18s</th>
  </tr>
  <tr>
    <td>Matrix Multiplication</td>
    <th>Python (Wheel)</th>
    <th>132.97s</th>
  </tr>
  <tr>
    <td>Matrix Inversion</td>
    <th>Python (Wheel)</th>
    <th>0.76s</th>
  </tr>
  <tr>
    <td>Matrix Multiplication</td>
    <th>Python (Source)</th>
    <th>39.23s</th>
  </tr>
  <tr>
    <td>Matrix Inversion</td>
    <th>Python (Source)</th>
    <th>17.75s</th>
  </tr>
  <tr>
    <td>Matrix Multiplication</td>
    <th>Python (Source + OpenBLAS)</th>
    <th>38.59s</th>
  </tr>
  <tr>
    <td>Matrix Inversion</td>
    <th>Python (Source + OpenBLAS)</th>
    <th>0.62s</th>
  </tr>
</table>
