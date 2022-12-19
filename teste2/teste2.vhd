library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity teste2 is

   port(
     A: in std_logic_vector(7 downto 0);
     B: in std_logic_vector(7 downto 0);
     C: in std_logic_vector(7 downto 0);
     Z: out std_logic_vector(7 downto 0);
     Z: out std_logic_vector(7 downto 0)   );
end teste2;

architecture Behavioral of teste2 is

component addsub8 is
    Port ( A : in STD_LOGIC_VECTOR (7 downto 0);
           B : in STD_LOGIC_VECTOR (7 downto 0);
           op : in STD_LOGIC;
           Y : out STD_LOGIC_VECTOR (7 downto 0));
end component;

signal sY_to_A8630 :STD_LOGIC_VECTOR( 7 DOWNTO 0 );
constant sconst_to_op62311 : std_logic:='0';
signal sY_to_out85413 :STD_LOGIC_VECTOR( 7 DOWNTO 0 );
constant sconst_to_op56115 : std_logic:='1';

begin

add1: addsub8
  port map(
     A=>A,
     B=>B,
     OP=>sconst_to_op62311,
     Y=>sY_to_A8630);

sub1: addsub8
  port map(
     A=>sY_to_A8630,
     B=>C,
     OP=>sconst_to_op56115,
     Y=>sY_to_out85413);


Z<=sY_to_out85413;
Z<=sc_to_out18717;

end behavioral;