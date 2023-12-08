/*
Créez un programme qui affiche son nom de fichier.


Exemples d’utilisation :
$> node exo.js
exo.js

$> node crevette.js
crevette.js
*/

package main

import (
	"fmt"
	"os"
	"path/filepath"
)

func main() {
	// Get the path of the executable
	execPath := os.Args[0]

	// Get the base of the path
	base := filepath.Base(execPath)
	fmt.Println(base + "(Terre001)")
}
