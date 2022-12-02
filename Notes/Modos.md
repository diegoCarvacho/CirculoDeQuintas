# Modos o modalidades de funcionamiento
## Alternativas para seleccionar el modo de ejecucion:
### Rotary Switch:
Al comenzar el rograma se llama a la funcion que revisa la posicion del rotary switch.
Dependiendo de la posicion del switch la variable "selectedMode" recibe un valor. (GateMode, LatchMode, ClockMode...)    
El programa principal al ser ejecutado va a ejecutar funciones basadas en el programa seleccionado.
usando el metodo del rotary Switch se puede leer el modo seleccinado en cualquier momento, sin 
necesidad de reiniciar el uC. De esta manera no se interrumpe el mensaje midi y de esta manera el audio.

- cómo usar un rotary switch que se connecte a 4 pins para decodificar la posicion de forma binaria? 
Creo que no se puede.
### Botones del círculo:
Al bootear el uC se va leer que boton o botones están siendo presionados y dependiendo de eso se seleccionara el modo. De esta manera no necesito un rotary switch ni usar mas GPIOs del RPico.
La desventaja de este modo es que se necesita reiniciar el uC para leer el modo actviado y se interrumpe el audio (midi).

## Ideas para distintos modos:
1. Gate = default. NoteOn se envia al presionar un boton y NoteOff al soltar el boton. Se puede presionar mas de un boton a la vez.
1. Latch(Hold) = AllNotesOff seguido con un NoteOn se envian al presionar un boton. Al soltar un boton no se envia nada. Por ende solo un acorde se puede hacer sonar a la vez.
1. Clock + Gate = Dependiendo de algunas variables que definan el tiempo. Al mantener presionado un boton se enviara un NoteOn y luego de un tiempo un NoteOff en Loop. Generando un Ritmo constante. Al soltar el boton se envia un NoteOff final y se termina el loop.
1. Clock + Gate = Al igual que el modo 4 se enviaran los NoteOn y NoteOff messages de forma ritmica. En este caso al soltar un boton no se enviara un noteOff final. De este manera el ultimo acorde presionado seguira siendo escuhado indefinidamente.
1.  Arpegiador
- cómo configurar cuantas octavas se usan?
- cómo configurar si el arpegio es ascendente o decendiente?
1. Sequenciador
- cómo grabar?
- cómo reproducir? se necesitan más botones!
- seria interesante agregarle un trigger input para poder usar el golbe de un bombo para ir pasando de un step al siguiente.



