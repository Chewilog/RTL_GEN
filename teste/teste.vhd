library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity teste is

   port(
     A: in std_logic_vector(7 downto 0);
     B: in std_logic_vector(7 downto 0);
     C: in std_logic_vector(7 downto 0);
     Z: out std_logic_vector(7 downto 0);
     J: out std_logic_vector(7 downto 0)   );
end teste;

architecture Behavioral of teste is

component addsub8 is
    Port ( A : in STD_LOGIC_VECTOR (7 downto 0);
           B : in STD_LOGIC_VECTOR (7 downto 0);
           op : in STD_LOGIC;
           Y : out STD_LOGIC_VECTOR (7 downto 0));
end component;

signal sY_to_A6900 :STD_LOGIC_VECTOR( 7 DOWNTO 0 );
constant sconst_to_op69611 : std_logic:='0';
signal sY_to_out84113 :STD_LOGIC_VECTOR( 7 DOWNTO 0 );
constant sconst_to_op29815 : std_logic:='1';
signal sc_to_out45117 :std_logic_vector(7 downto 0);

begin

add1: addsub8
  port map(
     A=>A,
     B=>B,
     OP=>sconst_to_op69611,
     Y=>sY_to_A6900);

sub1: addsub8
  port map(
     A=>sY_to_A6900,
     B=>C,
     OP=>sconst_to_op29815,
     Y=>sY_to_out84113);



process(sY_to_A6900,C)
begin
   sc_to_out45117<= unsigned(sY_to_A6900)+unsigned(C);
end process;


Z<=sY_to_out84113;
J<=sc_to_out45117;
 

end behavioral;