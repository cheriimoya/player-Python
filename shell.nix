with import <nixpkgs> { };
let
  python = pkgs.python3.withPackages (
    ps: with ps; [
      black
      flask
      flask-cors
      gunicorn
    ]
  );
in
mkShell { buildInputs = [ python ]; }
