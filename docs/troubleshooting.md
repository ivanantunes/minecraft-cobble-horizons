# Troubleshooting

## Menu principal continua vanilla

1. Confirme se config/fancymenu foi copiado para a raiz correta.
2. Confirme modpack_mode = true.
3. Verifique erros de layout no latest.log.
4. Confirme que os assets existem nos caminhos registrados.
5. Não edite o layout com o jogo aberto.

## Loading funciona, mas menus não

Drippy e FancyMenu usam configurações diferentes. O funcionamento do boot não confirma que o layout do title screen foi carregado.

## Texturas rosa/preto ou ausentes

Verifique nomes, extensão PNG, maiúsculas/minúsculas e caminhos source:local.

## Layout fora da tela

Teste GUI Scale 3, resolução 1920x1080 e modo janela. Registre resolução e escala usadas.

## Crash

Preserve latest.log e crash-reports. Informe a ação exata que causou o problema. Não remova mods aleatoriamente da instância principal; reproduza em uma cópia.