# Single Key Mode
Un rotary switch de 12 posiciones es instalado al centro del circulo.
Cada posicion del switch va a apuntar a uno de los 12 botones de cada circulo.
La idea es implementar un modo de funcionamiento que cambie el circulo de quintas a un circulo cromatico en el que la posicion del Switch selecciona el primer grado de la escala seleccionada (mayor, menor, frigio, penatonica, etc).
La escala se selecciona usando otro rotary switch.
> idealmente los botones deberian ser iluminados. De esta manera podrian iluminarse solamente los botones que correspondan a los acordes de la escala seleccionada.

### Rotary Central : C, escala seleccionada es mayor con triadas
- C
- Dm
- Em
- F
- G
- Am
- B°
### Rotary Central : A, escala seleccionada es menor con tetradas
- Am7
- Bm7b5
- Cmaj7
- Dm7
- Em7
- Fmaj7
- G7
### Rotary Central : C, escala seleccionada es  Frigia
- Cm7
- DbMaj7
- Eb7
- Fm7
- Gm7b5
- AbMaj7
- Bm7

## Ideas
### qué pasa si se toca un boton que no corresponda a la escala seleccionada?
si toco el boton del DO (boton 0) va sonar un acorde de DO mayor.
si toco el boton del DO# (boton 1) va a sonar??
opciones:
- nada
- algun acorde que contenga C# en sus notas, y pudiese ser utilizado como alteracion en la escala de Do mayor
- los botones que NO corresponden a algun grado de la escala seleccionada SOLAMENTE funcionan en conjunto con algun otro boton que SI corresponda a la escala seleccionada.
> Si la escala seleccionada es Do Mayor y se toca solamente el boton 1 (C#) entonces no suena nada, pero Si se mantiene presionado el boton 0 (C) y se presiona el boton 1 (C#) entonces se escucha un Cmaj7b9.
- algun acorde con el que se pudiese modular a otra escala y luego de tocar este acorde se deberia iluminar el boton que corresponde a la escala a la que se debe modular - indicando a qué posicion se debe cambiar el rotary.