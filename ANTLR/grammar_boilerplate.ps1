cd boilerplate
java -jar ../antlr-4.12.0-complete.jar -Dlanguage=Python3 -visitor ../grammars/Tua.g4
cd ..
cp boilerplate/* ../tua/interpreter/generated