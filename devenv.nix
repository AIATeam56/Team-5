{ pkgs, lib, config, inputs, ... }:

{
  cachix.enable = false;

  packages = [ pkgs.git pkgs.stdenv.cc.cc.lib pkgs.gcc-unwrapped pkgs.libz pkgs.jupyter ];
  env.LD_LIBRARY_PATH = "${pkgs.gcc-unwrapped.lib}/lib64:${pkgs.libz}/lib";

  languages.python = {
    enable = true;
    uv.enable = true;
    libraries = [pkgs.stdenv.cc.cc.lib pkgs.gcc-unwrapped pkgs.libz pkgs.jupyter];
  };

  enterShell = ''
    source .devenv/state/venv/bin/activate
  '';
}
