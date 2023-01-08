library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity teste2 is

   port(
     B: in std_logic_vector(7 downto 0);
     A: in std_logic_vector(7 downto 0);
     C: in std_logic_vector(7 downto 0);
     clk: in std_logic;
     rst: in std_logic;
     clr: in std_logic;
     ld: in std_logic;
     Z: out array_24b   );
end teste2;

architecture Behavioral of teste2 is

type array_24b is array(0 to 2) of std_logic_vector(7 downto 0);
constant N : integer:=3;
component reg8 is
    Port ( clk : in STD_LOGIC;
           rst : in STD_LOGIC;
           clr : in STD_LOGIC;
           ld : in STD_LOGIC;
           X : in STD_LOGIC_VECTOR(7 DOWNTO 0);
           Y : out STD_LOGIC_VECTOR(7 DOWNTO 0));
end component;

signal sf_to_out1240 :array_24b;
signal sc_to_clr9721 :STD_LOGIC;
signal sb_to_rst5771 :STD_LOGIC;
signal sa_to_clk3381 :STD_LOGIC;
signal se_to_X5631 :array_24b;
signal sd_to_ld4321 :STD_LOGIC;
signal sY_to_f9111 :array_24b;
signal sd_to_e5101 :array_24b;

begin



process(B,A,C)
begin
   sd_to_e5101<=B & A & C ;
end process;

gen_tot: FOR I IN 1 TO N GENERATE
  tot: reg8
      port map(
          clr => sc_to_clr9721,
          rst => sb_to_rst5771,
          clk => sa_to_clk3381,
          X => se_to_X5631(I),
          ld => sd_to_ld4321,
          Y => sY_to_f9111(I));
END GENERATE;

sc_to_clr9721<=clr;
sb_to_rst5771<=rst;
sa_to_clk3381<=clk;
se_to_X5631<=sd_to_e5101;
sd_to_ld4321<=ld;
sf_to_out1240<=sY_to_f9111;

Z<=sf_to_out1240;
 

end behavioral;