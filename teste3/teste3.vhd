library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity teste3 is

   port(
     clk: in std_logic;
     rst: in std_logic;
     Z: out std_logic_vector(15 downto 0);
     Z2: out std_logic_vector(15 downto 0)   );
end teste3;

architecture Behavioral of teste3 is

component PWM is
    generic( dutyCicle: std_logic := '0'
    );
    Port ( clk : in STD_LOGIC;
           rst : in STD_LOGIC;
           pwm : out STD_LOGIC
           );
end component;

component Counter is
    generic(max : integer:=10);
    Port ( clk : in STD_LOGIC;
           reset : in STD_LOGIC;
           en : in STD_LOGIC;
           updown : in STD_LOGIC;
           number : out integer);
end component;

component addsub8 is
    Port ( A : in STD_LOGIC_VECTOR (7 downto 0);
           B : in STD_LOGIC_VECTOR (7 downto 0);
           op : in STD_LOGIC;
           Y : out STD_LOGIC_VECTOR (7 downto 0));
end component;

signal sb_to_a5050 :std_logic_vector(31 downto 0);
signal spwm_to_clk1662 :STD_LOGIC;
signal snumber_to_A2654 :INTEGER;
signal sY_to_t9226 :STD_LOGIC_VECTOR( 7 DOWNTO 0 );
constant sconst_to_dutyCicle6488 : std_logic:='0';
constant sconst_to_en66215 : std_logic:='1';
constant sconst_to_updown44517 : std_logic:='1';
constant sconst_to_B53119 : std_logic_vector(7 downto 0):='00000001';
constant sconst_to_op94621 : std_logic:='1';
signal sb_to_out98323 :std_logic_vector(15 downto 0);
signal sc_to_out37124 :std_logic_vector(15 downto 0);

begin

clk_div: PWM
  port map(
     CLK=>clk,
     RST=>rst,
     PWM=>spwm_to_clk1662);

c1: Counter
  port map(
     CLK=>spwm_to_clk1662,
     RESET=>rst,
     EN=>sconst_to_en66215,
     UPDOWN=>sconst_to_updown44517,
     NUMBER=>snumber_to_A2654);

add1: addsub8
  port map(
     A=>std_logic_vector(to_unsigned(snumber_to_A2654,1)),
     B=>sconst_to_B53119,
     OP=>sconst_to_op94621,
     Y=>sY_to_t9226);



with sY_to_t9226 select sb_to_a5050
  "00000000000000000000000000000000" when "00000000",
  "00111111001101010000010011110011" when "00000001",
  "00111111100000000000000000000000" when "00000010",
  "00111111001101010000010011110011" when "00000011",
  "00100101000011010011000100110010" when "00000100",
  "10111111001101010000010011110011" when "00000101",
  "10111111100000000000000000000000" when "00000110",
  "10111111001101010000010011110011" when "00000111",
  "00000000000000000000000000000000" when others;

sb_to_out98323<=sb_to_a5050(31 downto 16);
sc_to_out37124<=sb_to_a5050(15 downto 0);


Z<=sb_to_out98323;
Z2<=sc_to_out37124;
 

end behavioral;