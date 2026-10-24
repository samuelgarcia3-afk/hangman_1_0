## Lista de tareas identificadas

- [x] Crear el repositorio público en GitHub con README (nombre, correo y forma de ejecución)
- [x] Crear archivo con la lista de palabras (`palabras.py`)
- [ ] Crear archivo con las 6 etapas del monigote (`monigote.py`)
- [ ] Importar lista de palabras y monigote en el archivo principal
- [ ] Seleccionar una palabra aleatoria y mostrarla como `_ _ _ _`
- [ ] Pedir una letra por consola
- [ ] Validar que sea solo 1 letra
- [ ] Validar que esté entre A-Z
- [ ] Validar que no se haya usado antes
- [ ] Reemplazar los guiones por la letra en todas las posiciones donde aparezca
- [ ] Manejar 6 vidas: restar una vida por error y mostrar contador y dibujo
- [ ] Derrota: contador en 0, último dibujo, mensaje de perdida y revelar la palabra
- [ ] Victoria: mostrar mensaje de ganaste
- [ ] Menú para finalizar o jugar de nuevo

> [!NOTE]
> Marcar cada tarea con `[x]` en el commit en que se resuelve.

# Juego del ahorcado (hangman_1_0)

## Autor

- **Nombre:** Samuel García
- **Correo:** samuel.garcia3@utp.edu.co

## Estructura

| Archivo | Descripción |
|---|---|
| `hangman.py` | Programa principal |
| `palabras.py` | Lista de palabras |
| `monigote.py` | Etapas del dibujo |

## Cómo ejecutar

```bash
cd hangman_1_0
python hangman.py
```

> [!IMPORTANT]
> Se requiere Python 3.6 o superior. Los tres archivos deben estar en la misma carpeta.

> [!TIP]
> Ingrese una letra a la vez. Entradas como `123` o `ABC` muestran el mensaje "Debe ingresar solo 1 letra".

> [!WARNING]
> Solo se aceptan letras de la A a la Z, sin tildes ni ñ.
