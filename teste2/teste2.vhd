library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity teste2 is

   port(
     tot_ld: in std_logic;
     tot_clr: in std_logic;
     clk: in std_logic;
     a: in std_logic_vector(7 downto 0);
     s: in std_logic_vector(7&nbsp;downto 0);
     rst: in std_logic;
     tot_lt_s: out std_logic   );
end teste2;

architecture Behavioral of teste2 is

component reg8 is
    Port ( clk : in STD_LOGIC;
           rst : in STD_LOGIC;
           clr : in STD_LOGIC;
           ld : in STD_LOGIC;
           X : in STD_LOGIC_VECTOR(7 DOWNTO 0);
           Y : out STD_LOGIC_VECTOR(7 DOWNTO 0));
end component;

component Comparator is
    Port ( a : in integer;
           b : in integer;
           op : in STD_LOGIC_VECTOR(2 downto 0);
           cmpout : out STD_LOGIC);
end component;

component addsub8 is
    Port ( A : in STD_LOGIC_VECTOR (7 downto 0);
           B : in STD_LOGIC_VECTOR (7 downto 0);
           op : in STD_LOGIC;
           Y : out STD_LOGIC_VECTOR (7 downto 0));
end component;

signal sY_to_B8600 :STD_LOGIC_VECTOR( 7 DOWNTO 0 );
signal scmpout_to_out8663 :STD_LOGIC;
signal sY_to_X2145 :STD_LOGIC_VECTOR( 7 DOWNTO 0 );
constant sconst_to_op90719 : std_logic_vector(2 downto 0):="010";
constant sconst_to_op74521 : std_logic:='0';

begin

tot: reg8
  port map(
     CLK=>clk,
     RST=>rst,
     CLR=>tot_clr,
     LD=>tot_ld,
     X=>sY_to_X2145,
     Y=>sY_to_B8600);

cmp0: Comparator
  port map(
     A=>to_integer(unsigned(sY_to_B8600)),
     B=>to_integer(unsigned(s)),
     OP=>sconst_to_op90719,
     CMPOUT=>scmpout_to_out8663);

adder0: addsub8
  port map(
     A=>a,
     B=>sY_to_B8600,
     OP=>sconst_to_op74521,
     Y=>sY_to_X2145);


tot_lt_s<=scmpout_to_out8663;

end behavioral;