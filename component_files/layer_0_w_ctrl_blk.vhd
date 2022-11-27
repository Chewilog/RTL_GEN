----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 15.08.2022 15:00:14
-- Design Name: 
-- Module Name: layer_0_w_ctrl_blk - Behavioral
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
-- arithmetic functions with Signed or Unsigned values
use IEEE.NUMERIC_STD.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;
use work.config_const.all;
use work.types_pack.all;
-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx leaf cells in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity layer_0_w_ctrl_blk is
    generic(k_index:integer:=0);
    Port ( cnt : in STD_LOGIC_VECTOR (N_size_bits-1 downto 0);
           index : out STD_LOGIC_VECTOR (N_size_bits-2 downto 0));
end layer_0_w_ctrl_blk;

architecture Behavioral of layer_0_w_ctrl_blk is


begin
    
process(cnt)
begin
    if unsigned(cnt)<N_size_bits then
        index<=std_logic_vector(to_unsigned(layer0w_vals(to_integer(unsigned(cnt)))(k_index),N_size_bits-1));
    else
        index<=(others=>'0');
    end if;
end process;





end Behavioral;
