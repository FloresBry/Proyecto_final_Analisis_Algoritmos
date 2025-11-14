#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <vector>

namespace py = pybind11;

std::vector<int> buscar_patron_binario(const std::vector<int>& texto, const std::vector<int>& patron) {
    std::vector<int> posiciones;
    int n = texto.size(), m = patron.size();
    if (n < m) return posiciones;

    for (int i = 0; i <= n - m; ++i) {
        bool coincide = true;
        for (int j = 0; j < m; ++j) {
            if (texto[i + j] != patron[j]) {
                coincide = false;
                break;
            }
        }
        if (coincide) posiciones.push_back(i);
    }
    return posiciones;
}

PYBIND11_MODULE(busqueda, m) {
    m.def("buscar_patron_binario", &buscar_patron_binario, "Buscar patrón binario en texto comprimido");
}
