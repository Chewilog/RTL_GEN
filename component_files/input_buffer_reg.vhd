----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 02.07.2022 12:32:12
-- Design Name: 
-- Module Name: input_buffer_reg - Behavioral
-- Project Name: 
-- Target Devices: 
-- Tool Versions: 
-- Description: 
-- 
-- Dependencies: 
-- 
-- Revision:
-- Revision 0.01 - File Created
-- Additional Comments:
-- 
----------------------------------------------------------------------------------


library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx leaf cells in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity input_buffer_reg is
    Port ( clk : in STD_LOGIC;
           rst: in STD_LOGIC;
           x : in STD_LOGIC_VECTOR (7 downto 0);
           l_buffer : in STD_LOGIC;
           c_buffer : in STD_LOGIC;
           reg_output : out STD_LOGIC_VECTOR (7 downto 0));
end input_buffer_reg;

architecture Behavioral of input_buffer_reg is



begin


reg_input_number:process(clk,rst,c_buffer,l_buffer)
    begin
        if c_buffer='1' or rst='1' then
            reg_output <= (others=>'0');
        elsif rising_edge(clk) then
            if l_buffer = '1' then
                reg_output <= x;
            end if; 
        end if;
    end process;

end Behavioral;
