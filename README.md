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
    <td>J</td>
    <td>1.41s</td>
  </tr>
  <tr>
    <td>Matrix Inversion</td>
    <td>J</td>
    <td>3.87s</td>
  </tr>
  <tr>
    <td>Matrix Multiplication</td>
    <td>Python (MKL)</td>
    <td>40.1s</td>
  </tr>
  <tr>
    <td>Matrix Inversion</td>
    <td>Python (MKL)</td>
    <td>0.59s</td>
  </tr>
  <tr>
    <td>Matrix Multiplication</td>
    <td>Python (Ubuntu)</td>
    <td>18.21s</td>
  </tr>
  <tr>
    <td>Matrix Inversion</td>
    <td>Python (Ubuntu)</td>
    <td>18.18s</td>
  </tr>
  <tr>
    <td>Matrix Multiplication</td>
    <td>Python (Wheel)</td>
    <td>132.97s</td>
  </tr>
  <tr>
    <td>Matrix Inversion</td>
    <td>Python (Wheel)</td>
    <td>0.76s</td>
  </tr>
  <tr>
    <td>Matrix Multiplication</td>
    <td>Python (Source)</td>
    <td>39.23s</td>
  </tr>
  <tr>
    <td>Matrix Inversion</td>
    <td>Python (Source)</td>
    <td>17.75s</td>
  </tr>
  <tr>
    <td>Matrix Multiplication</td>
    <td>Python (Source + OpenBLAS)</td>
    <td>38.59s</td>
  </tr>
  <tr>
    <td>Matrix Inversion</td>
    <td>Python (Source + OpenBLAS)</td>
    <td>0.62s</td>
  </tr>
</table>
