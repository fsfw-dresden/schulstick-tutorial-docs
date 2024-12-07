{
  description = "Documentation about creating Tutorials for Lernstick";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-24.11";
  };

  outputs = { self, nixpkgs, ... }:
  let
    system = "x86_64-linux";
    pkgs = import nixpkgs {inherit system;};
    inherit (pkgs) lib;
    nativeBuildInputs = with pkgs; [
      mdbook
      mdbook-linkcheck
      mdbook-mermaid
    ];
  in rec {
    devShells.${system} = {
      ci = pkgs.mkShell {
        inherit nativeBuildInputs;
        shellHook = ''
          mdbook-mermaid install
          mdbook build
          touch book/.nojekyll
          exit
        '';
      };
      default = pkgs.mkShell {
        inherit nativeBuildInputs;
        shellHook = ''
          mdbook-mermaid install
          mdbook serve --port 3333 --open
          exit
        '';
      };
    };
  };
}
