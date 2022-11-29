library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity teste is
   generic(
   max0 : integer := 10   );

   port(
     upORdown: in std_logic;
     enable: in std_logic;
     clk: in std_logic;
     rst: in std_logic;
     ilt8: out std_logic;
     aux: out std_logic;
     iteste: out std_logic   );
end teste;

architecture Behavioral of teste is

component Counter is
    generic(max : integer:=10);
    Port ( clk : in STD_LOGIC;
           reset : in STD_LOGIC;
           en : in STD_LOGIC;
           updown : in STD_LOGIC;
           number : out integer);
end component;

component Comparator is
    Port ( a : in integer;
           b : in integer;
           op : in STD_LOGIC_VECTOR(2 downto 0);
           cmpout : out STD_LOGIC);
end component;

signal snumber_to_a475 :INTEGER;
signal scmpout_to_out637 :STD_LOGIC;
constant const_b306 : integer:=8;
constant const_op773 : std_logic_vector(2 downto 0):="000";
signal scmpout_to_out188 :STD_LOGIC;
constant const_a246 : std_logic_vector(3 downto 0):="1000";
constant const_op229 : std_logic_vector(2 downto 0):="101";

begin

cntr: Counter
  generic map(
    max => max0);

  port map(
     CLK=>clk;
     RESET=>rst;
     EN=>enable;
     UPDOWN=>upORdown;
     NUMBER=>snumber_to_a475);

cmp0: Comparator
  port map(
     A=>snumber_to_a475;
     B=>sconst_to_b119;
     OP=>sconst_to_op932;
     CMPOUT=>scmpout_to_out637);

cmp1: Comparator
  port map(
     A=>to_integer(unsigned(sconst_to_a985));
     B=>sconst_to_b119;
     OP=>sconst_to_op912;
     CMPOUT=>scmpout_to_out188);


ilt8<=scmpout_to_out637;
aux<=sin_to_updown851;
iteste<=scmpout_to_out188;

end behavioral;